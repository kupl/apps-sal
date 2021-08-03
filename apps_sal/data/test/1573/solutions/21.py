n, d = list(map(int, input().split()))

persons = []

for i in range(n):
    m, s = list(map(int, input().split()))
    persons.append((m, s))

persons.sort()
max_s = 0
cur_s = persons[0][1]
good_persons = [persons[0]]
for i in range(1, n):
    if abs(good_persons[0][0] - persons[i][0]) < d:
        good_persons.append(persons[i])
        cur_s += persons[i][1]
    else:
        j = 0
        rec_s = 0
        while (j < len(good_persons)) and (abs((good_persons[j][0] - persons[i][0])) >= d):
            rec_s += good_persons[j][1]
            j += 1
        if rec_s <= persons[i][1]:
            cur_s = cur_s - rec_s + persons[i][1]
            good_persons = good_persons[j:] + [persons[i]]
        else:
            max_s = max(max_s, cur_s)
            cur_s = cur_s - rec_s + persons[i][1]
            good_persons = good_persons[j:] + [persons[i]]


print(max(cur_s, max_s))
