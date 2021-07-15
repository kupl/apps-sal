import sys
sys.setrecursionlimit(100000000)

def main():
    N,K = map(int,input().split())
    sushi = [tuple(map(int,input().split())) for _ in range(N)]

    sushi.sort(key = lambda x:x[1],reverse = True)
    ans = 0
    dic = {}
    change = []
    for a,b in sushi[:K]:
        if a in dic:
            dic[a].append(b)
            change.append((a,b))
        else:
            dic[a] = [b]
        ans += b

    various = len(dic)
    ans += various ** 2
    ret = ans
    used_type = set(dic.keys())
    suggestion = [p for p in sushi[K:] if p[0] not in used_type]
    for a,b in suggestion:
        if len(change) == 0:
            break
        if a in used_type:
            continue
        dic[change[-1][0]].pop()
        ret -= change[-1][1]
        ret += b + 2*various + 1
        dic[a] = b
        change.pop()
        various += 1
        used_type.add(a)
        ans = max(ans,ret)
    print(ans)
def __starting_point():
    main()
__starting_point()
