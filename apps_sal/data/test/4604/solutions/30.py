from collections import Counter
n = int(input())
a = sorted(list(map(int, input().split())))
a_count = Counter(a)
if n % 2 == 1:
    ans = 1
    for i in a_count:
        if i % 2 != 0:
            print(0)
            break
        elif i == 0:
            if a_count[i] != 1:
                print(0)
                break
        elif a_count[i] == 2:
            ans = ans * 2 % (10 ** 9 + 7)
        else:
            print(0)
            break
    else:
        print(ans)
else:
    ans = 1
    for j in a_count:
        if j % 2 != 1:
            print(0)
            break
        elif a_count[j] == 2:
            ans = ans * 2 % (10 ** 9 + 7)
        else:
            print(0)
            break
    else:
        print(ans)
