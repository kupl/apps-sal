

good = set('AHIMOTUVWXY')

in_str = input("")

str_len = len(in_str)

result = ""

i = 0

while(i < str_len / 2):
    if((in_str[i] in good) and (in_str[i] == in_str[-1 - i])):
        i += 1
    else:
        result = "NO"
        break

if(result != "NO"):
    result = "YES"

print(result)
