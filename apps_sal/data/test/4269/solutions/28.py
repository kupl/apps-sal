s = list(input())

judge = 'Good'

for i in range(len(s)-1):
    if s[i]==s[i+1]:
        judge = 'Bad'
        break
print(judge)
