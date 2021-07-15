from fractions import Fraction as F

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def line_y(x: int, x_0:int, y_0:int, d_x: int, d_y: int) -> int:
            '''
                Return the y coordinate of given x for the line defined by (x_0, y_0) and (d_x, d_y)
            '''
            return F(d_y, d_x) * (x - x_0) + y_0
        
        def line_x(y: int, x_0: int, y_0: int, d_x: int, d_y: int) -> int:
            '''
                Return the x coordinate of given y for the line defined by (x_0, y_0) and (d_x, d_y)
            '''
            return (y - y_0) / F(d_y, d_x) + x_0
            
        # (x, y) start position of the ray
        # (d_x, d_y) direction of the ray
        x_0, y_0, d_x, d_y = 0, 0, p, q
        
        while True:
            if d_x > 0:
                # Toward right                
                y_intercept_right = line_y(p, x_0, y_0, d_x, d_y)

                if y_intercept_right == p:
                    return 1
                elif y_intercept_right == 0:
                    return 0
                elif 0 < y_intercept_right < p:
                    # hit right
                    x_0, y_0, d_x, d_y = p, y_intercept_right, -d_x, d_y
                elif y_intercept_right > p:
                    # hit top
                    x_0, y_0, d_x, d_y = line_x(p, x_0, y_0, d_x, d_y), p, d_x, -d_y
                else:
                    # y_intercept_right < 0
                    # hit bottom
                    x_0, y_0, d_x, d_y = line_x(0, x_0, y_0, d_x, d_y), 0, d_x, -d_y
            else:
                # Toward left
                y_intercept_left = line_y(0, x_0, y_0, d_x, d_y)

                if y_intercept_left == p:
                    return 2
                elif 0 < y_intercept_left < p:
                    # hit left
                    x_0, y_0, d_x, d_y = 0, y_intercept_left, -d_x, d_y
                elif y_intercept_left > p:
                    # hit top
                    x_0, y_0, d_x, d_y = line_x(p, x_0, y_0, d_x, d_y), p, d_x, -d_y
                else:
                    # y_intercept_left < 0
                    # hit bottom
                    x_0, y_0, d_x, d_y = line_x(0, x_0, y_0, d_x, d_y), 0, d_x, -d_y
