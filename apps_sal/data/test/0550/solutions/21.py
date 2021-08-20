def make_hash(string):
    return string.lower().replace('o', '0').replace('l', '1').replace('i', '1')


s = make_hash(input())
n = int(input())
e = []
good = True
for _ in range(n):
    t = input()
    if make_hash(t) == s:
        good = False
print('Yes' if good else 'No')
