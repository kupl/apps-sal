import sys
my_file = sys.stdin
num = int(my_file.readline())
dist = my_file.readline().strip("\n").split(" ")
coords = my_file.readline().strip("\n").split(" ")
dist = [int(i) for i in dist]
coords = [int(i) for i in coords]
start = coords[0] - 1
end = coords[1] - 1
if start > end:
    temp = start
    start = end
    end = temp
len1 = sum(dist[start:end:])
len2 = sum(dist[end:len(dist):]) + sum(dist[:start:])
if len1 < len2:
    print(len1)
else:
    print(len2)
