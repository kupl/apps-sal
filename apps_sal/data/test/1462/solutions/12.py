def main():
    (n, k) = [int(i) for i in input().split(' ')]
    cards = input()
    letters = []
    for i in range(n):
        if cards[i] not in letters:
            letters.append(cards[i])
    l = len(letters)
    freq = [0 for i in range(l)]
    for i in range(l):
        freq[i] = cards.count(letters[i])
    total = 0
    while k != 0:
        m = max(freq)
        if m > k:
            total = total + k * k
            k = 0
        else:
            k = k - m
            total = total + m * m
            freq.remove(m)
    print(total)


main()
