S = input()
List = list(S)
trial = 0
for i in range(1, len(List)):
    if List[i] != List[i - 1]:
        trial += 1
print(trial)
