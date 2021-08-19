from heapq import *
import sys
input = sys.stdin.readline


def main():
    n, q = list(map(int, input().split()))
    children = [[int(x) for x in input().split()] for _ in range(n)]

    m = int(2 * 1e5)
    heap_each = [[] for _ in range(m)]
    each_moved = [dict() for _ in range(m)]
    heap_all = []
    all_moved = dict()
    for i in range(n):
        a, b = children[i]
        heappush(heap_each[b - 1], -a)
    for i in range(m):
        if heap_each[i]:
            heappush(heap_all, -heap_each[i][0])

    ans = []
    for i in range(q):
        c, d = list(map(int, input().split()))  # 幼児Cが幼稚園Dに移動
        a, b = children[c - 1]  # 幼児のレート：A、元の幼稚園：B
        if a == -heap_each[b - 1][0]:  # 幼児がその園のトップだったとき
            if a in all_moved:  # 全体リストから削除
                all_moved[a] += 1
            else:
                all_moved[a] = 1
            heappop(heap_each[b - 1])  # その幼稚園のリストから削除
            while heap_each[b - 1]:  # 値が削除済みの園児かどうか判定:そうでないなら全体リストに値を追加
                if heap_each[b - 1][0] in each_moved[b - 1] and each_moved[b - 1][heap_each[b - 1][0]] > 0:
                    each_moved[b - 1][heap_each[b - 1][0]] -= 1
                    heappop(heap_each[b - 1])
                    continue
                heappush(heap_all, -heap_each[b - 1][0])
                break
        else:  # 幼児がその園のトップでないときは、削除リストに追加するのみ
            if -a in each_moved[b - 1]:
                each_moved[b - 1][-a] += 1
            else:
                each_moved[b - 1][-a] = 1
        # 転園先での話
        if not heap_each[d - 1]:  # 新しい園がひとりぼっちなら
            heappush(heap_each[d - 1], -a)
            heappush(heap_all, a)
        elif -a < heap_each[d - 1][0]:  # 新しい園でトップなら
            if -heap_each[d - 1][0] in all_moved:  # 旧一位を全体リストから削除
                all_moved[-heap_each[d - 1][0]] += 1
            else:
                all_moved[-heap_each[d - 1][0]] = 1
            heappush(heap_each[d - 1], -a)
            heappush(heap_all, a)
        else:  # 新しい園でただの人なら
            heappush(heap_each[d - 1], -a)
        while heap_all:
            if heap_all[0] in all_moved and all_moved[heap_all[0]] > 0:
                all_moved[heap_all[0]] -= 1
                heappop(heap_all)
                continue
            break
        children[c - 1][1] = d
        ans.append(heap_all[0])

    for answer in ans:
        print(answer)


def __starting_point():
    main()


__starting_point()
