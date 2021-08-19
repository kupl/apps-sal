t = int(input())
for test_index in range(t):
    n = int(input())
    list_of_students = []
    for i in range(n):
        l, r = map(int, input().split())
        list_of_students.append((i, l, r))
    sorted_list = sorted(list_of_students, key=lambda x: (x[1], x[0]), reverse=True)
#    print(sorted_list)
    current_time = 1
    answer = [0 for i in range(n)]
    while (len(sorted_list) > 0):
        current_customer = sorted_list.pop()
        if current_time < current_customer[1]:
            current_time = current_customer[1]
#        print(current_time, current_customer)
        if current_time > current_customer[2]:
            continue
        answer[current_customer[0]] = current_time
        current_time += 1
    for x in answer:
        print(x, end=" ")
    print()
