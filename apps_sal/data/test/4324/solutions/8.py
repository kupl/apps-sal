from string import ascii_lowercase
chars = ascii_lowercase
for _ in range(int(input())):
    (n, a, b) = list(map(int, input().split()))
    print(''.join([chars[i % b] for i in range(n)]))
