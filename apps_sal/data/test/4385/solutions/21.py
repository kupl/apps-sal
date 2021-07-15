abcde = [int(input()) for _ in range(5)]
k = int(input())

for i in range(4):
    for j in range(i, 5):
        if abcde[j] - abcde[i] > k:
            print(':(')
            return
print('Yay!')
