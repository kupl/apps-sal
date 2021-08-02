string = input()
numadd = int(input())
lval1 = input().split(' ')
lval = [int(x) for x in lval1]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maxvalue = lval.index(max(lval))
string += numadd * alphabet[maxvalue]
perfect = 0
for charsa in range(1, len(string) + 1):
    perfect += charsa * int(lval[alphabet.index(string[charsa - 1])])
print(perfect)
