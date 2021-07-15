n = int(input())
pilhas = list(map(int, input().split()))

count = [0] * 51

for pilha in pilhas:
    count[pilha] += 1

for i in range(51):
    if count[i] != 0 and count[i] * 2 <= n:
        print("Alice")
        break
    elif count[i] != 0 and count[i] * 2 > n:
        print("Bob")
        break
