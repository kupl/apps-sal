import random


def MillerRabinPrimalityTest(number):
    """
    because the algorithm input is ODD number than if we get
    even and it is the number 2 we return TRUE ( spcial case )
    if we get the number 1 we return false and any other even 
    number we will return false.
    """
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0:
        return False
    ' first we want to express n as : 2^s * r ( were r is odd ) '
    ' the odd part of the number '
    oddPartOfNumber = number - 1
    ' The number of time that the number is divided by two '
    timesTwoDividNumber = 0
    ' while r is even divid by 2 to find the odd part '
    while oddPartOfNumber % 2 == 0:
        oddPartOfNumber = oddPartOfNumber // 2
        timesTwoDividNumber = timesTwoDividNumber + 1
    '\n    since there are number that are cases of "strong liar" we \n    need to check more then one number\n    '
    for time in range(3):
        ' choose "Good" random number '
        while True:
            ' Draw a RANDOM number in range of number ( Z_number )  '
            randomNumber = random.randint(2, number) - 1
            if randomNumber != 0 and randomNumber != 1:
                break
        ' randomNumberWithPower = randomNumber^oddPartOfNumber mod number '
        randomNumberWithPower = pow(randomNumber, oddPartOfNumber, number)
        ' if random number is not 1 and not -1 ( in mod n ) '
        if randomNumberWithPower != 1 and randomNumberWithPower != number - 1:
            iterationNumber = 1
            ' while we can squre the number and the squered number is not -1 mod number'
            while iterationNumber <= timesTwoDividNumber - 1 and randomNumberWithPower != number - 1:
                ' squre the number '
                randomNumberWithPower = pow(randomNumberWithPower, 2, number)
                iterationNumber = iterationNumber + 1
            '     \n            if x != -1 mod number then it because we did not found strong witnesses\n            hence 1 have more then two roots in mod n ==>\n            n is composite ==> return false for primality\n            '
            if randomNumberWithPower != number - 1:
                return False
    ' well the number pass the tests ==> it is probably prime ==> return true for primality '
    return True


cases = int(input())
for case in range(cases):
    (a, b) = map(int, input().split())
    t = MillerRabinPrimalityTest(a ** 2 - b ** 2)
    if t:
        print('YES')
    else:
        print('NO')
