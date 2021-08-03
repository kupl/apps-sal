n, m, k = list(map(int, input().split()))
mi = list(map(int, input().split()))

ans = 0
items_to_del = 0
shift = 1
c_page = None
for el in mi:
    if c_page is None:
        c_page = (el - shift) // k
        items_to_del = 1
    else:
        page = (el - shift) // k
        if page != c_page:
            shift += items_to_del
            ans += 1
            c_page = (el - shift) // k
            items_to_del = 1
        else:
            items_to_del += 1
if items_to_del != 0:
    ans += 1
print(ans)
