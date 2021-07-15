s = input()
if "." not in s:
    s += "."

left,right = s.strip("0").split(".")

if not left:
    t = right.strip("0")
    e = len(t) - len(right) - 1
    l = t[0]
    r = t[1:]
else:
    e = len(left)-1
    l = left[0]
    r = (left[1:]+right).rstrip("0")

if l:
    print(l,end='')
else:
    print(0,end='')

if r:
    print("."+r,end='')

if e:
    print("E%d"%e)
