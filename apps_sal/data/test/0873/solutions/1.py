n = int(input())
string1 = input()
string2 = input()
answer = 0
for i in range(n):
    answer += min(abs(int(string1[i]) - int(string2[i])), 10 - abs(int(string1[i]) - int(string2[i])))
print(answer)
