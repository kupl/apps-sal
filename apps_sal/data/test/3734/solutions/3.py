def main():
    a = input().strip()
    b = input().strip()
    q = [28, 30, 31]
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    f = False
    for x in q:
        if (days.index(a) + x) % 7 == days.index(b):
            f = True
            break
    if f:
        print("YES")
    else:
        print("NO")
main()
