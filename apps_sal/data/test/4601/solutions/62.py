N, K = map(int, input().split())
lst = list(map(int, input().split()))

if N <= K:
    print(0)

else:
    lst.sort(reverse=True)
    lst = lst[K:]
    print(sum(lst))
