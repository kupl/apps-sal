s = input().strip()
k = int(input())
if len(s) < k:
    print("impossible")
else:
    s_set = set(map(str, list(s)))
    if len(s_set) >= k:
        print(0)
    else:
        print(k - len(s_set))

