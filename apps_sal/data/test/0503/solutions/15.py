(inp, inp1) = map(int, input().split())
inp2 = list(map(int, input().split()))
dictionary = {}
dictionaryFNums = {}
k = inp1
res = 0
for n in range(inp):
    element = inp2[n]
    if element % k == 0:
        res += dictionary.get(element / k, 0)
        dictionary[element] = dictionary.get(element, 0) + dictionaryFNums.get(element / k, 0)
    dictionaryFNums[element] = dictionaryFNums.get(element, 0) + 1
print(res)
