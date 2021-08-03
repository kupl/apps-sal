N = int(input())
List = list(input().split())
List = list(map(int, List))
List_sorted = sorted(List)

i = 0
while i < len(List) - 1:
    j = i + 1
    ListTest = list(List)
    count = 0
    while j < len(List):
        if ListTest == List_sorted:
            print('YES')
            return
        ListTest[i], ListTest[j] = ListTest[j], ListTest[i]
        if ListTest == List_sorted:
            print('YES')
            return
        else:
            ListTest = list(List)
        j += 1
    i += 1
print('NO')
