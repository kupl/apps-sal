s = int(input())
L = [1, 1, 1]
if s < 3:
    print(0)
elif s < 6:
    print(1)
elif 6 <= s:
    for i in range(s - 5):
        L.append((L[-1] + L[-3]) % (10 ** 9 + 7))
    print(L[-1])
