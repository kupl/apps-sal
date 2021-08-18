
person_count = int(input())
person_list = [input().split(" ") for _ in range(person_count)]
order = [int(x) - 1 for x in input().split(" ")]
string = ""
for number in order:
    if string <= person_list[number][0] and string <= person_list[number][1]:
        string = min(person_list[number])
    elif string <= person_list[number][0]:
        string = person_list[number][0]
    elif string <= person_list[number][1]:
        string = person_list[number][1]
    else:
        print("NO")
        break
else:
    print("YES")
