class Solution:
    '''
    - light yellow
    - if left is blue
        - keep on marking everything to the right blue
    - if in the end number of yello = 0, increment ans
    - key thing to notice is that the blue only start propogating when number 1 bulb is lighted

    '''

    def numTimesAllBlue(self, light: List[int]) -> int:
        nyellow = 0
        nblue = 0
        dx = {}
        YELLOW = 0
        BLUE = 1
        OFF = 2
        for b in light:
            dx[b] = OFF
        ans = 0
        for i in range(len(light)):

            curr = light[i]
            dx[curr] = YELLOW
            nyellow += 1
            check = False

            if curr == 1 or dx[curr - 1] == BLUE:
                check = True
            if check:
                for j in range(curr, len(light) + 1):
                    if dx[j] == OFF:
                        break
                    else:
                        nyellow -= 1
                        nblue += 1
                        dx[j] = BLUE

            if nyellow == 0:
                ans += 1
        return ans
