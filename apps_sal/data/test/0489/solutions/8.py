from collections import Counter

def main():
    int(input())
    a = list(map(int, input().split()))

    a.sort()
    x, y, z = a[:3]
    freq = Counter(a)

    if x == y and y == z:
        ans = freq[x] * (freq[x] - 1) * (freq[x] - 2) // 6
    elif x == y:
        ans = freq[x] * (freq[x] - 1) * freq[z] // 2
    elif x == z:
        ans = freq[x] * (freq[x] - 1) * freq[y] // 2
    elif y == z:
        ans = freq[y] * (freq[y] - 1) * freq[x] // 2
    else:
        ans = freq[x] * freq[y] * freq[z]

    print(ans)

main()

