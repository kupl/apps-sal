n = int(input())
string = input()
chaine = 'ACTG'
mini = float('inf')
for i in range(len(string) - 3):
    mini = min(mini, sum([min(abs(ord(string[ind]) - ord(a)), 26 - abs(ord(string[ind]) - ord(a))) for (a, ind) in zip(chaine, list(range(i, i + 4)))]))
print(mini)
