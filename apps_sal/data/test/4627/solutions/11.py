"""
Author: Q.E.D
Time: 2020-05-24 08:43:25
"""
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    (odd, even) = ([], [])
    for x in a:
        if x % 2 == 1:
            odd.append(x)
        else:
            even.append(x)
    if len(odd) % 2 == 0 and len(even) % 2 == 0:
        ans = 'YES'
    else:
        for i in range(len(odd)):
            valid = False
            for j in range(len(even)):
                if abs(odd[i] - even[j]) == 1:
                    valid = True
                    break
            if valid:
                break
        ans = 'YES' if valid else 'NO'
    print(ans)
