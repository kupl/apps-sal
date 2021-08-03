x = input()
is_mirror = "YES"
bad_list = ["B", "C", "D", "E", "F", "G", "J", "K", "L", "N", "P", "Q", "R", "S", "Z"]
for letter in x:
    if letter in bad_list:
        is_mirror = "NO"
        break
list = []
if is_mirror == "YES":
    for letter in x:
        list.append(letter)
n = len(list)
for i in range(n - 1):
    if list[i] != list[n - 1 - i]:
        is_mirror = "NO"
print(is_mirror)
