(n, k) = [int(i) for i in input().split()]
'\n1 2 3 4 5 6 7\n1 2 3 | 4 5 6 7\nsplit into 2k groups\n\nif last group < k then problem\n\nif k = 3, n = 7\n\n1 2 3 4 5 6 7\n\n1 2 3 4 5\n\nfirst sz varies from k+1 to 2*k+1\n\n\n1 (k+1 - 2k+1) + x(2*k) + 1(2k+1 - k+1)\n1 2 3 4 5 6 7 8 9 10\n\n11,2 = 1 6 10\n8, 2 = 1 6\n'
(places, placee) = (0, 0)
ans = 2 * n
for start in range(k + 1, 2 * k + 2):
    for end in range(k + 1, 2 * k + 2):
        if (n - start - end) % (2 * k + 1) == 0:
            if 2 + (n - start - end) // (2 * k + 1) < ans:
                ans = min(ans, 2 + (n - start - end) // (2 * k + 1))
                places = start
                placee = end
print(ans)
print(places - k, end=' ')
if ans > 1:
    for j in range((n - places - placee) // (2 * k + 1)):
        print(places - k + (j + 1) * (2 * k + 1), end=' ')
    last = placee - k - 1
    print(n - last)
