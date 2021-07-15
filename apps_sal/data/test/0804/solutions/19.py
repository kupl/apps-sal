a = input()
k = int(input())
l = [0] * 26
if len(a) < k or k > 26:
    print("impossible")
else:
    for i in a:
        l[ord(i) - ord('a')] = 1
    if sum(l) >= k:
        print(0)
    else:
        print(k - sum(l))
