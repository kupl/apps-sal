n = int(input())
flats = input()
types = set(flats)
counter = {}
menor = n
j = 0
for i in range(n):
    if flats[i] not in counter:
        counter[flats[i]] = 0
    counter[flats[i]] += 1
    if len(counter) < len(types):
        continue
    while counter[flats[j]] > 1:
        counter[flats[j]] -= 1
        j += 1
    menor = min(menor, i-j+1)
    if menor == len(types):
        break
print(menor)

