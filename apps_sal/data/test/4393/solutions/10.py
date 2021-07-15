amount = int(input())
string = input()
answer = ''
counter = 1
i = 0
while i < len(string):
    answer += string[i]
    i += counter
    counter += 1
print(answer)
