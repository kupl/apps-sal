def main():
    string=input()
    fulcrum=string.index('^')
    mass_left=0
    mass_right=0
    for i in range(0,fulcrum):
        if string[i] != '=':
            mass_left+=int(string[i]) * (fulcrum-i)
    for i in range(fulcrum+1,len(string)):
        if string[i] != '=':
            mass_right+=int(string[i])*(i-fulcrum)

    if mass_left==mass_right:
        print ("balance")
        return
    if mass_left<mass_right:
        print("right")
        return
    if mass_right<mass_left:
        print("left")
        return
def __starting_point():
    main()
__starting_point()
