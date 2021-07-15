def main():
    N = int(input())
    result = {"AC": 0, "WA": 0, "TLE": 0, "RE":0}

    for i in range(N):
        result[input()] += 1

    print(( "AC x " + str(result["AC"]) ))
    print(("WA x " + str(result["WA"])))
    print(("TLE x " + str(result["TLE"])))
    print(("RE x " + str(result["RE"])))

main()

