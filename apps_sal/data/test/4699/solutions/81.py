N, K = [int(x) for x in input().split()]
D = input().split()

for payment in range(N, 10 * N + 1):
    if all(char not in D for char in str(payment)):
        print(payment)
        break
