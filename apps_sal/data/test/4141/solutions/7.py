N = int(input())
List = list(map(int, input().split()))
List_2 = list(filter(lambda x: x % 2 == 0, List))
answer = 'APPROVED'
for x in List_2:
    if x % 3 != 0 and x % 5 != 0:
        answer = 'DENIED'
print(answer)
