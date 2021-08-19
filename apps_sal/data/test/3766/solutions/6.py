n = int(input())
colour = dict(zip('RGBYW', range(5, 10)))
cards = list({2 ** colour[c] + 2 ** (ord(v) - ord('1')) for (c, v) in input().split()})
ans = 10
n = len(cards)
if n > 1:
    for bit in range(2 ** 10):
        ok = True
        for i in range(n - 1):
            for j in range(i + 1, n):
                if cards[i] & cards[j] == 0:
                    if (cards[i] | cards[j]) & bit == 0:
                        ok = False
                        break
                elif cards[i] != cards[j]:
                    if (cards[i] ^ cards[j]) & bit == 0:
                        ok = False
                        break
            if not ok:
                break
        if ok:
            ans = min(bin(bit).count('1'), ans)
    print(ans)
else:
    print(0)
