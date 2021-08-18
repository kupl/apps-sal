N = int(input())

S = input()

target = 'ABC'
counter = 0

for i in range(0, len(S) - 2):
    if S[i:i + 3] == target:
        counter += 1

print(counter)
