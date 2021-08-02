from heapq import heappush, heapify, heappop


def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    que = []
    heapify(que)
    heappush(que, (-A[0] - B[0] - C[0], 0, 0, 0))
    s = set()

    for i in range(K):
        ans = heappop(que)
        print(-ans[0])
        if(ans[1] < X - 1 and not (ans[1] + 1, ans[2], ans[3]) in s):
            heappush(que, [-A[ans[1] + 1] - B[ans[2]] - C[ans[3]], ans[1] + 1, ans[2], ans[3]])
            s.add((ans[1] + 1, ans[2], ans[3]))
        if(ans[2] < Y - 1 and not (ans[1], ans[2] + 1, ans[3]) in s):
            heappush(que, [-A[ans[1]] - B[ans[2] + 1] - C[ans[3]], ans[1], ans[2] + 1, ans[3]])
            s.add((ans[1], ans[2] + 1, ans[3]))
        if(ans[3] < Z - 1 and not (ans[1], ans[2], ans[3] + 1) in s):
            heappush(que, [-A[ans[1]] - B[ans[2]] - C[ans[3] + 1], ans[1], ans[2], ans[3] + 1])
            s.add((ans[1], ans[2], ans[3] + 1))


main()
