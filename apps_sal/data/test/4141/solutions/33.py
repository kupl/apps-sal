n = int(input())
integer_list = list(map(int, input().split()))
even_list = list()
approve_counts = 0

for i in integer_list:
    if i % 2 == 0:
        even_list.append(i)

for j in even_list:
    if j % 3 == 0 or j % 5 == 0:
        approve_counts += 1

if approve_counts == len(even_list):
    print('APPROVED')
else:
    print('DENIED')
