n, k = list(map(int, input().split()))
s = input()

abc = set(s)
mi = min(abc)
ma = max(abc)

if k > n:
    print(s + min(abc) * (k - n))

else:
    S = sorted(abc)

    temp = s[:k]

    for i, el in enumerate(s[:k][::-1]):
        if el != ma:
            print(s[:k - i - 1] + S[S.index(el) + 1] + mi * i)
            break
