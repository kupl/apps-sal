str_input = input()
k = int(input())
w = [int(s) for s in input().split()]
value = 0
for i in range(len(str_input)):
    value += (i + 1) * int(w[ord(str_input[i]) - 97])


def lam(x): return (x + 1 + len(str_input)) * int(max(w))


for i in range(k):
    value += lam(i)
print(value)
