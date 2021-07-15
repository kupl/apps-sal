def main():
    n = int(input())
    amounts = [int(i) for i in input().split()]
    cnt = dict()
    prefix = 0
    for a in amounts:
        prefix += a
        if prefix in cnt:
            cnt[prefix] += 1
        else:
            cnt[prefix] = 1
    ans = 0
    for k in cnt:
        if ans < cnt[k]:
            ans = cnt[k]
    print(n - ans)

main()

