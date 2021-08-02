n, k = [int(i) for i in input().split()]

'''
1 2 3 4 5 6 7
1 2 3 | 4 5 6 7
split into 2k groups

if last group < k then problem

if k = 3, n = 7

1 2 3 4 5 6 7

1 2 3 4 5

first sz varies from k+1 to 2*k+1


1 (k+1 - 2k+1) + x(2*k) + 1(2k+1 - k+1)
1 2 3 4 5 6 7 8 9 10

11,2 = 1 6 10
8, 2 = 1 6
'''

places, placee = 0, 0
ans = 2 * n
for start in range(k + 1, 2 * k + 2):
    for end in range(k + 1, 2 * k + 2):
        if (n - (start) - (end)) % (2 * k + 1) == 0:
            if 2 + (n - (start) - (end)) // (2 * k + 1) < ans:
                ans = min(ans, 2 + (n - (start) - (end)) // (2 * k + 1))
                places = start
                placee = end

print(ans)
print(places - k, end=' ')
if ans > 1:
    for j in range((n - places - placee) // (2 * k + 1)):
        print(places - k + (j + 1) * (2 * k + 1), end=' ')
    last = placee - k - 1
    print(n - last)
    #print(places - k + (j+1)*(2*k+1))
