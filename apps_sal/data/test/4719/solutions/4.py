alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = dict()
for a in alphabet:
    key[a] = 50
n = int(input())
for i in range(n):
    x = input()
    for a in alphabet:
        key[a] = min(key[a], x.count(a))
for (k, v) in key.items():
    for _ in range(v):
        print(k, end='')
print()
