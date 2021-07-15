def str_to_int(s):
    if s == "^":
        return 0
    if s == ">":
        return 1
    if s == "v":
        return 2
    if s == "<":
        return 3

inputlist = list(map(str_to_int, input().strip().split(" ")))
start = inputlist[0]
end = inputlist[1]
duration = int(input())

if (start + duration) % 4 == end and (start - duration) % 4 != end:
    print("cw")
elif (start - duration) % 4 == end and (start + duration) % 4 != end:
    print("ccw")
else:
    print("undefined")
