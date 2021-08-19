n = int(input())
alphabet_count = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for alpha in alphabet:
    alphabet_count[alpha] = 1000000000
mojis = []
for i in range(n):
    mojis.append(input())


def get_count(moji):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_count = {}
    for alpha in alphabet:
        alphabet_count[alpha] = 0
    for m in moji:
        alphabet_count[m] += 1
    return alphabet_count


for moji in mojis:
    each_count = get_count(moji)
    for alpha in alphabet:
        alphabet_count[alpha] = min(alphabet_count[alpha], each_count[alpha])
ans = ''
for alpha in alphabet:
    for i in range(alphabet_count[alpha]):
        ans = ans + alpha
print(ans)
