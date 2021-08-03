offering_number = int(input())
offering_color = set(i for i in input().split())
if len(offering_color) == 3:
    print("Three")
else:
    print("Four")
