def good_angle(angle):
    exterior = 180 - angle
    if exterior == 0:
        return "NO"
    n = 360 / exterior
    if n == (int(n)):
        return "YES"
    else:
        return "NO"


def main():
    first_line = input()
    
    n = int(first_line)
    angles = []

    for i in range(n):
        angle = input()
        angles += [int(angle)]

    for a in angles:
        print(good_angle(a))
        
    


main()   

