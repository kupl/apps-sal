from fractions import gcd


def Irreducible_Fraction(A, B):
    ''' Returns list of two integers representing the nominator and denominator of the Irreducible version of A/B '''
    x = gcd(A, B)
    return [A // x, B // x]


a, b, c, d = map(int, input().split())

F = a / b

S = c / d


(a / b < c / d)
(a / b == c / d)
(a / b > c / d)


if(a / b < c / d):
    stretching_factor = a / c
    New_horizontal = a
    New_vertical = a * d
    New_Movie_Area = int(New_horizontal * New_vertical)
    Screen_Area = int(a * b * c)
    Empty_Area = Screen_Area - New_Movie_Area
    desired_ratio = Irreducible_Fraction(Empty_Area, Screen_Area)
    nominator = desired_ratio[0]
    denominator = desired_ratio[1]
    print(nominator, end="/")
    print(denominator)


elif(a / b == c / d):
    print("0/1")


else:
    stretching_factor = b / d
    New_vertical = b
    New_horizontal = (b) * c
    New_Movie_Area = int(New_horizontal * New_vertical)
    Screen_Area = int(a * b * d)
    Empty_Area = Screen_Area - New_Movie_Area
    desired_ratio = Irreducible_Fraction(Empty_Area, Screen_Area)
    nominator = desired_ratio[0]
    denominator = desired_ratio[1]
    print(nominator, end="/")
    print(denominator)
